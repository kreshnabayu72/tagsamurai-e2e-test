---
id: TC-FA-FAAL-E2E-015-defense-in-depth-akses-ditolak-group-manager
title: "Defense-in-Depth: Direct API, Download, dan SSE Group Manager Ditolak"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAL-256
  - TC-FA-FAAL-257
  - TC-FA-FAAL-258
coverage:
  web: automated
---

# Defense-in-Depth: Direct API, Download, dan SSE Group Manager Ditolak

## Prerequisites

- Mode: FE+BE.
- Akun yang dipakai:

  | Peran dalam spec | Pre-setup | Email | Env var password |
  |---|---|---|---|
  | Group Manager (Group Manager untuk group Gedung A), klien HTTP dan SSE dengan token sesi | #8 | `groupManagerFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` |
  | Total Control (Admin Alpha), sesi UI pembanding dan sesi API | #1 | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
- Login akun aktor pertama (Group Manager, Pre-setup #8) di hook `before` spec ini; token sesi Group Manager dibaca untuk klien HTTP dan SSE. Halaman dibuka hook `beforeEach` suite (Fixed Asset > Reports & Logs > Activity Log); langkah 1 sampai 14 tidak memakai halaman itu. Hook `after` memulihkan nama group `Gedung G` lalu mengembalikan sesi UI ke akun default suite (Total Control, Pre-setup #1).
- Kemampuan teknis disediakan tim FE: klien HTTP dan SSE dengan token sesi, serta dua sesi browser untuk SSE (butir "Kemampuan teknis tambahan" di `suite.md`). Endpoint daftar log, export, dan SSE tidak ditulis di TC (lihat Temuan untuk QA) dan disediakan tim BE/FE, tanpa endpoint karangan.
- Sesi API aktor (butir "Sesi API aktor" di `suite.md`): admin Alpha (#1) mengubah nama group lewat sesi API yang tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE.
- Env var `FA_GM_PASSWORD` dan `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (R-07). Password dan token tidak ditulis di spec atau fixture.
- Data: Tab User Action UA-01 sampai UA-15 (Pre-setup #12) dipulihkan ke keadaan Pre-setup sebelum spec (disediakan tim FE/BE). Group `Gedung G` (Pre-setup #18, Dinamis #6) diubah menjadi `Gedung G1` pada TC-FA-FAAL-258 dan dipulihkan ke `Gedung G`.
- State global yang diubah spec: nama group `Gedung G`. Pemulihan di langkah 23 dan hook `after`.
- Jendela asersi absence SSE: 5 detik tanpa memuat ulang halaman adalah pilihan spec (bagian 6), bukan nilai TC atau PRD.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`). Berlaku untuk akun #8 dan #1.
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-256: Permintaan langsung daftar log oleh Group Manager ditolak server

1. Kirim permintaan GET daftar Tab Session langsung ke API dengan token sesi Group Manager, tanpa lewat UI
2. Verifikasi respons permintaan daftar Tab Session: 403 Forbidden
3. Verifikasi respons permintaan daftar Tab Session: tidak memuat satu pun baris log
4. Kirim permintaan GET daftar Tab User Action langsung ke API dengan token sesi Group Manager
5. Verifikasi respons permintaan daftar Tab User Action: 403 Forbidden
6. Verifikasi respons permintaan daftar Tab User Action: tidak memuat satu pun baris log

### TC-FA-FAAL-257: Permintaan langsung Download oleh Group Manager ditolak server

7. Kirim permintaan export CSV Tab Session langsung ke API dengan token sesi Group Manager
8. Verifikasi respons export CSV Tab Session: 403 Forbidden
9. Verifikasi respons export CSV Tab Session: tidak menghasilkan berkas
10. Kirim permintaan export XLSX Tab User Action langsung ke API dengan token sesi Group Manager
11. Verifikasi respons export XLSX Tab User Action: 403 Forbidden
12. Verifikasi respons export XLSX Tab User Action: tidak menghasilkan berkas

### TC-FA-FAAL-258: Group Manager tidak dapat membuka koneksi SSE Activity Log

13. Coba buka koneksi SSE Activity Log langsung dengan token sesi Group Manager
14. Verifikasi koneksi Group Manager tidak pernah terbentuk (ditolak sebelum channel dibuka, bukan koneksi tanpa event)
15. Ganti akun: Logout dari akun Group Manager, lalu Login sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`) dan buka Fixed Asset > Reports & Logs > Activity Log
16. Klik tab User Action
17. Verifikasi koneksi SSE sesi Total Control terbentuk
18. Catat baseline jumlah entri Tab User Action dari teks pagination
19. Pada sesi API admin Total Control (#1), ubah nama group `Gedung G` menjadi `Gedung G1` hingga tersimpan
20. Verifikasi sesi Total Control menerima baris baru dari aksi Edit Group tanpa memuat ulang halaman (jumlah entri bertambah satu dari baseline)
21. Tunggu 5 detik tanpa memuat ulang halaman
22. Verifikasi Group Manager tidak menerima event apa pun
23. Pada sesi API admin Total Control (#1), ubah nama group `Gedung G1` menjadi `Gedung G` hingga tersimpan

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular. TC-FA-FAAL-256, 257, dan 258 ada di spec ini; TC-FA-FAAL-259, 260, dan 262 ada di spec 066.
- K-1: TC-FA-FAAL-256 dan 257 adalah TC defense-in-depth dengan Expected respons API; tetap masuk spec FE+BE walau tumpang tindih dengan `tc-activity-log-backend.md` (tidak ada), karena TC granular tetap sumber dan tiap TC tepat satu spec.
- Langkah 1 sampai 12 mengirim request lewat klien HTTP, tidak melewati browser; asersi hanya status respons dan isi respons (bagian 8b butir 1). Perilaku FE untuk respons yang sama diasersi di spec jalur UI.
- P-2: TC-FA-FAAL-258 memakai sesi UI Total Control sebagai pembanding bagi asersi utama (klien Group Manager tidak menerima event), bukan sebagai objek uji mandiri. Pelaku kedua yang memicu Edit Group memakai sesi API dan tidak butuh butir `P-2`.
- Langkah penghubung (S-03): langkah 15 (ganti akun, lalu membuka Activity Log), langkah 16 dan 18 (tab User Action dan baseline, S-12), langkah 19 dan 23 (pemicu Edit Group dan pemulihan nama group lewat sesi API; langkah 19 ditulis "... hingga ... tersimpan", R-20).
- Langkah 22 (absence) didahului anchor positif langkah 20 (sesi Total Control menerima baris dari aksi yang sama) dan jendela 5 detik langkah 21 (bagian 6).
- Ukuran spec 23 langkah, di bawah ambang.
- Temuan untuk QA:
  - TC-FA-FAAL-256 sampai 258 tidak menyebut endpoint daftar log, export, dan SSE; spec tidak mengarang endpoint (S-13) dan menyerahkannya ke tim BE/FE.
  - TC-FA-FAAL-258 langkah 3 menyebut "satu aksi Edit Group" tanpa menyebut group dan nama baru; spec memakai `Gedung G` (Pre-setup #18) menjadi `Gedung G1` dan memulihkannya.
  - TC-FA-FAAL-258 tidak menyebut apakah koneksi SSE Total Control diamati pada tab Session atau User Action; spec memakai tab User Action karena Edit Group dicatat di sana.
  - TC-FA-FAAL-256 sampai 258 tidak menyebut env var password; nama env var diusulkan dari butir "Env var" di `suite.md`.
